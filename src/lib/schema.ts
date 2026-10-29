import { SITE } from './site';
import { BUSINESS, CLINIC_ADDRESS } from './legal';

/**
 * Structured data (schema.org JSON-LD). The business entity is emitted on
 * every page so search engines can tie each page to the clinic; articles add
 * their own BlogPosting that points back to it by @id.
 *
 * Only confirmed details go in. Opening hours, social profiles and the MOH
 * registration are still TBC in lib/legal.ts and are left out rather than
 * guessed: wrong structured data is worse than missing structured data.
 * No priceRange, because the brief rules out price framing.
 */
const BUSINESS_ID = `${SITE}/#business`;
const WEBSITE_ID = `${SITE}/#website`;

const str = (v: unknown) => (typeof v === 'string' ? v : undefined);

export const businessSchema = {
  '@type': 'MedicalBusiness',
  '@id': BUSINESS_ID,
  name: 'Cellove Wellness',
  description:
    'A doctor-led cellular wellness centre in Kuala Lumpur, at Pavilion Damansara Heights, minutes from Petaling Jaya.',
  url: SITE,
  logo: `${SITE}/media/logo-cellove.svg`,
  image: `${SITE}/media/clinic-entrance.webp`,
  email: str(BUSINESS.email),
  telephone: str(BUSINESS.whatsapp),
  address: {
    '@type': 'PostalAddress',
    streetAddress: CLINIC_ADDRESS.street,
    postalCode: CLINIC_ADDRESS.postcode,
    addressLocality: CLINIC_ADDRESS.city,
    addressRegion: CLINIC_ADDRESS.region,
    addressCountry: CLINIC_ADDRESS.country,
  },
  areaServed: [
    { '@type': 'City', name: 'Kuala Lumpur' },
    { '@type': 'City', name: 'Petaling Jaya' },
  ],
};

export const websiteSchema = {
  '@type': 'WebSite',
  '@id': WEBSITE_ID,
  name: 'Cellove Wellness',
  url: SITE,
  inLanguage: 'en-MY',
  publisher: { '@id': BUSINESS_ID },
};

export function articleSchema(a: {
  url: string;
  title: string;
  description: string;
  date: Date;
  image: string;
}) {
  return {
    '@type': 'BlogPosting',
    '@id': `${a.url}#article`,
    mainEntityOfPage: a.url,
    headline: a.title,
    description: a.description,
    datePublished: a.date.toISOString(),
    image: new URL(a.image, SITE).href,
    inLanguage: 'en-MY',
    author: { '@id': BUSINESS_ID },
    publisher: { '@id': BUSINESS_ID },
    isPartOf: { '@id': WEBSITE_ID },
  };
}

/** Wrap entities in one @graph document. */
export function graph(...nodes: object[]) {
  return { '@context': 'https://schema.org', '@graph': nodes };
}
