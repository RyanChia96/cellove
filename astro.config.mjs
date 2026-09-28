// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import icon from 'astro-icon';

/**
 * Windows dev-server stability.
 *
 * Vite registers the bare drive root ("C:\") as a watch path. Chokidar then
 * crawls it and calls lstat on locked Windows system files such as
 * C:\DumpStack.log.tmp, which raises EBUSY as an unhandled 'error' event on the
 * FSWatcher and kills `astro dev` outright. The crash is timing-dependent on
 * when Windows touches those files, so it presents as the server dying at
 * random intervals.
 *
 * Ignoring the bare drive root stops that crawl. Project paths are watched via
 * their own deeper roots and are unaffected, so hot reload still works. The
 * system-file list below is belt and braces for the same class of failure.
 */
const BACKSLASH = String.fromCharCode(92);

const SYSTEM_ENTRIES = new Set([
  'dumpstack.log',
  'dumpstack.log.tmp',
  'pagefile.sys',
  'swapfile.sys',
  'hiberfil.sys',
  'system volume information',
  '$recycle.bin',
  '$winreagent',
  'config.msi',
  'recovery',
]);

function toPosix(candidate) {
  return String(candidate).split(BACKSLASH).join('/');
}

/** A bare drive root such as "C:/" or "C:". Never useful to watch. */
function isDriveRoot(posixPath) {
  return /^[a-z]:\/?$/i.test(posixPath);
}

function isUnwatchable(candidate) {
  const posix = toPosix(candidate);
  if (isDriveRoot(posix)) return true;
  return posix
    .toLowerCase()
    .split('/')
    .some((segment) => SYSTEM_ENTRIES.has(segment));
}

export default defineConfig({
  site: 'https://cellove.my',
  integrations: [icon({ include: { ph: ['*'] } })],
  vite: {
    plugins: [tailwindcss()],
    server: {
      watch: {
        ignored: [
          isUnwatchable,
          '**/node_modules/**',
          '**/.git/**',
          '**/dist/**',
          '**/.astro/**',
        ],
      },
    },
  },
});
