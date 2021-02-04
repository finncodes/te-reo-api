# Māori Dictionary API

This Flask app provides an API that allows you to get the Māori translations/definitions available on https://maoridictionary.co.nz. The keyword(s) is specified using a query string parameter `?keyword=` and the results are returned in JSON, which consists of an array of words and their definitions and example sources.