import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export const focusInput = [
  // base
  "focus:ring-2",
  // ring color
  "focus:ring-blue-200 focus:dark:ring-blue-700/30",
  // border color
  "focus:border-blue-500 focus:dark:border-blue-700",
];

// Tremor Raw focusRing [v0.0.1]

export const focusRing = [
  // base
  "outline outline-offset-2 outline-0 focus-visible:outline-2",
  // outline color
  "outline-blue-500 dark:outline-blue-500",
];

// Tremor Raw hasErrorInput [v0.0.1]

export const hasErrorInput = [
  // base
  "ring-2",
  // border color
  "border-red-500 dark:border-red-700",
  // ring color
  "ring-red-200 dark:ring-red-700/30",
];

/**
 * Generate a localized path by prepending the locale to the path.
 * If the path already starts with a locale, it will be replaced.
 * @param path - The path to localize (e.g., "/contact", "/spending")
 * @param locale - The locale code (e.g., "en", "fr")
 * @returns The localized path (e.g., "/en/contact", "/fr/spending")
 */
export function localizedPath(path: string, locale: string): string {
  // Remove leading slash for processing
  const cleanPath = path.startsWith("/") ? path.slice(1) : path;

  // Check if path already starts with a locale
  const locales = ["en", "fr"];
  const pathParts = cleanPath.split("/");
  const firstPart = pathParts[0];

  // If first part is a locale, replace it; otherwise prepend the locale
  if (locales.includes(firstPart)) {
    pathParts[0] = locale;
  } else {
    pathParts.unshift(locale);
  }

  return "/" + pathParts.join("/");
}
