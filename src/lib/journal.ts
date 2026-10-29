import { getCollection, type CollectionEntry } from 'astro:content';

export type Post = CollectionEntry<'journal'>;

/** Published posts, newest first. */
export async function getPosts(): Promise<Post[]> {
  const posts = await getCollection('journal', (p) => !p.data.draft);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}

/** Read time from the actual word count at 200 words a minute, never typed in by hand. */
export function readTime(post: Post): string {
  const words = (post.body ?? '').trim().split(/\s+/).filter(Boolean).length;
  return `${Math.max(1, Math.round(words / 200))} min read`;
}

export function formatDate(d: Date): string {
  return d.toLocaleDateString('en-MY', { day: 'numeric', month: 'long', year: 'numeric' });
}

/** Cards for the index and the homepage teaser: real posts first, then the
 *  placeholder cards to fill the row until there are three real posts.
 *  Placeholders link to the Journal index, never to a URL that would 404. */
export type Card = { k: string; d: string; meta: string; img: string; href: string; alt: string };

const PLACEHOLDERS: Card[] = [];

export async function getCards(limit = Infinity): Promise<{ cards: Card[]; count: number }> {
  const posts = await getPosts();
  const real: Card[] = posts.map((p) => ({
    k: p.data.title.replace(/\.$/, ''),
    d: p.data.description,
    meta: readTime(p),
    img: p.data.image,
    href: `/journal/${p.id}`,
    alt: p.data.imageAlt,
  }));
  return { cards: [...real, ...PLACEHOLDERS].slice(0, limit), count: posts.length };
}
