/** Single source of truth for the conversation entry point.
 *  The brief (section 25) requires the pre-filled message to open on
 *  understanding rather than on price. */
export const WHATSAPP_NUMBER = '60123456789'; // TODO: replace with the clinic's real WhatsApp business number
export const WHATSAPP_MESSAGE =
  'Hi Cellove, I would like to learn more about your approach to cellular wellness.';
export const WHATSAPP_HREF = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(WHATSAPP_MESSAGE)}`;
