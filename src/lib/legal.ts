/**
 * Every business detail the legal pages need but which the client has not
 * supplied yet. One place to fill in, so nothing is hunted through prose.
 *
 * NOTHING HERE IS INVENTED. Each value is a marker that renders as a visible
 * highlighted placeholder on the page, so an unresolved detail cannot ship
 * unnoticed. Replace the value with the real string to clear the highlight.
 *
 * These documents are drafts prepared for review. They are not legal advice
 * and must be signed off by a Malaysian lawyer before publication, alongside
 * the medical review the brief already requires.
 */
export const TBC = Symbol('to be confirmed');
export type Detail = string | typeof TBC;

/** The clinic address in parts, for structured data. BUSINESS.clinicAddress
 *  is built from it so the two cannot drift apart. */
export const CLINIC_ADDRESS = {
  street: '02-16-03A, Pavilion Damansara Heights, No 3, Jalan Damanlela, Pusat Bandar Damansara',
  postcode: '50490',
  city: 'Kuala Lumpur',
  region: 'Wilayah Persekutuan Kuala Lumpur',
  country: 'MY',
};

export const BUSINESS = {
  /** Registered legal name, which may differ from the trading name. */
  legalName: TBC as Detail,
  /** SSM company registration number. */
  registrationNo: TBC as Detail,
  /** Registered business address. */
  address: TBC as Detail,
  /** Clinic address, if different from the registered address. */
  clinicAddress: `${CLINIC_ADDRESS.street}, ${CLINIC_ADDRESS.postcode} ${CLINIC_ADDRESS.city}` as Detail,
  /** General enquiries email. */
  email: 'cellovewellness@gmail.com' as Detail,
  /** Landline or business phone. */
  phone: TBC as Detail,
  /** WhatsApp business number. Currently a placeholder in lib/site.ts too. */
  whatsapp: '+60 11-4533 1349' as Detail,
  /** Named contact for PDPA requests, and their email. */
  dataProtectionContact: TBC as Detail,
  dataProtectionEmail: TBC as Detail,
  /** MOH / KKM facility registration number, if the centre holds one. */
  mohRegistrationNo: TBC as Detail,
  /** Who hosts the site and where the data physically sits. */
  hostingProvider: TBC as Detail,
  /** Where contact-form submissions are delivered and stored. */
  formProcessor: TBC as Detail,
  /** How long enquiry records are kept before deletion. */
  retentionPeriod: TBC as Detail,
  /** Opening hours, for the contact page. */
  openingHours: TBC as Detail,
} satisfies Record<string, Detail>;

/** Date these drafts were last edited. Update when the content changes. */
export const LEGAL_LAST_UPDATED = '5 October 2026';
