# Web Scraping Script

This script takes in a csv which contains Linkedin URLs along with the names of html files containing Linkedin profile information. It outputs a csv where each row contains a Linkedin URL along with the corresponding high school.

The input csv should be named input_linkedin_profiles.csv. Each row should consist of the URL as the first element and the html file as the second element, and the first row should be actual data: fieldnames should not be included. The Education section (if it exists) of each HTML file should be directly inside the &lt;h1&gt; tag, and it should have a list as its only sibling - inside of each list should be the schools listed in the Education section (where each school name is directly inside of a &lt;h3&gt; tag, and all descriptions listed under that school are not using a header tag). Four examples of properly formatted html files have been included in this repo, as well as a sample input csv file (also named input_linkedin_profiles.csv).

The output csv file (named output_high_schools.csv) contains a header containing field names. See the example output file (output_high_schools.csv) provided in this repo.

Libraries needed to run this script are re, csv, and beautiful soup.