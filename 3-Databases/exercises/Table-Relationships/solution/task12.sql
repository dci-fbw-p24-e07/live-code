SELECT
  locale.name AS "Locale",
  language.name AS "Language",
  country.name AS "Country"
FROM locale, language, country
WHERE
  locale.language_code = language.code AND
  locale.country_code = country.code
ORDER BY language.name;
