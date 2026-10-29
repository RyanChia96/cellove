/**
 * Results posters for the homepage Testimonials section. These are the
 * client's own campaign posters, used as supplied, except that the patient's
 * hospital record number (MRN) has been blacked out on both lab reports in
 * the cholesterol poster. Never publish a version with the MRN visible.
 *
 * MEDICAL AND LEGAL REVIEW REQUIRED before launch. The posters carry outcome
 * claims and before/after photographs, which Malaysian health advertising
 * rules (Medicine (Advertisement and Sale) Act 1956, Medical Advertisements
 * Board) restrict, including anything concerning diabetes.
 *
 * The alt text carries each poster's wording, so the claims are readable by
 * screen readers and search engines, not only as pixels.
 */
export type Poster = { src: string; width: number; height: number; alt: string };

export const POSTERS: Poster[] = [
  {
    src: '/media/results-hair.webp', width: 853, height: 1280,
    alt: 'Before and after photographs of the crown of a man\'s head. Healthier scalp, stronger, fuller hair. Stimulates hair follicles, improves scalp health, strengthens hair shafts, restores natural volume.',
  },
  {
    src: '/media/results-skin.webp', width: 854, height: 1280,
    alt: 'Before and after photographs of a woman\'s cheek. Real healing, faster than you think: healing in 1 week. Accelerates healing, rebuilds skin barrier, reduces scarring, restores natural glow.',
  },
  {
    src: '/media/results-foot.webp', width: 853, height: 1280,
    alt: 'Before and after photographs of a foot wound. Diabetic foot healing in 3 weeks. Speeds up wound healing, reduces inflammation, improves circulation, prevents further complications. Individual results vary; diabetic foot wounds require professional medical care.',
  },
  {
    src: '/media/results-cholesterol.webp', width: 864, height: 1080,
    alt: 'Two lab reports, before and after. Better cholesterol results in under four months: LDL 3.4 to 2.5 mmol/L, 26% lower; total cholesterol 5.4 to 4.3, 20% lower; non-HDL 4.1 to 3.2, 22% lower. One patient\'s results; individual results and cholesterol targets vary.',
  },
];
