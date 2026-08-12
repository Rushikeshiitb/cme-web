import { getPermalink } from './utils/permalinks';

export const headerData = {
  links: [
    { text: 'About', href: getPermalink('/about') },
    { text: 'Curriculum', href: getPermalink('/curriculum') },
    { text: 'Concentrations', href: getPermalink('/concentrations') },
    { text: 'Faculty', href: getPermalink('/people') },
    { text: 'Students', href: getPermalink('/students') },
    { text: 'Placements', href: getPermalink('/placements') },
    { text: 'Admissions', href: getPermalink('/admissions') },
  ],
  actions: [{ text: 'Contact', href: getPermalink('/contact') }],
};

export const footerData = {
  links: [
    {
      title: 'Programme',
      links: [
        { text: 'About CME', href: getPermalink('/about') },
        { text: 'Curriculum & Structure', href: getPermalink('/curriculum') },
        { text: 'BS Concentrations', href: getPermalink('/concentrations') },
        { text: 'Admissions', href: getPermalink('/admissions') },
      ],
    },
    {
      title: 'Community',
      links: [
        { text: 'IDPC Faculty', href: getPermalink('/people') },
        { text: 'Students & Seminars', href: getPermalink('/students') },
        { text: 'Placements', href: getPermalink('/placements') },
        { text: 'Contact', href: getPermalink('/contact') },
      ],
    },
    {
      title: 'Resources',
      links: [
        { text: 'IIT Bombay', href: 'https://www.iitb.ac.in' },
        { text: 'EE Department', href: 'https://www.ee.iitb.ac.in' },
        { text: 'Email the office', href: 'mailto:rajeshzele@iitb.ac.in' },
      ],
    },
  ],
  secondaryLinks: [],
  socialLinks: [],
  footNote: `
    © 2026 Centre for Multidisciplinary Education, IIT Bombay. Formerly the Centre for Liberal Education (CLE).
  `,
};
