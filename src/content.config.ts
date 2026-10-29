import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * The Cellove Journal. One Markdown file per post in src/content/journal; the
 * filename is the URL slug.
 *
 * MEDICAL AND LEGAL REVIEW REQUIRED for every post before it is published.
 * Set `draft: true` to keep a post off the site while it is in review.
 */
const journal = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/journal' }),
  schema: z.object({
    title: z.string(),
    /** Line under the title on the post page. */
    standfirst: z.string(),
    /** Meta description and card summary. Keep it under ~155 characters. */
    description: z.string(),
    date: z.coerce.date(),
    image: z.string(),
    imageAlt: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { journal };
