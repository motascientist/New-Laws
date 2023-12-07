## Motivation

I undertook a project involving the extraction of legal data from a reputable source with the objective of developing an application to present this information to politicians. Despite completing the project successfully and presenting the collected data, the agreed-upon compensation was not provided. In response, I gracefully accepted the situation and decided to showcase the project in my public portfolio.

### The Process

- **Step 1: Selecting Good Font**

    I've searched in many websites where extract legal fonts and I've found https://leismunicipais.com.br/ a complete font to collect all recent laws approved.

- **Step 2: Starting the Process**

    With over 5500 municipalities in Brazil, manually selecting each one is a daunting task given the extensive number. Consequently, a more efficient approach would involve scraping the municipality list from the website: https://leismunicipais.com.br/cidades-por-estado/ . So is that what consist *munincipios_list.py* and automatically store the data in *munincipios.txt*

- **Step 3: Collecting the laws**

   I initially developed a code, named *local_scraper.py*, for local testing purposes. I find it more convenient to have a local setup as it allows for easier testing and experimentation with changes. The code exports the data in a .json format, as the eventual application will be using JavaScript. JSON is preferred for its readability in JavaScript. This approach enhances the development and testing process.

- **Step 4 - Submitting to AWS**

    After write the *Dockerfile* I make the changes in the code to run in a EC2 and store the data in a S3 Bucket, the *scraper.py* has the changes
 
