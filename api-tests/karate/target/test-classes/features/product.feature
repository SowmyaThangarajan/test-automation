Feature: Product API Contract Validation

Background:
  * url baseUrl
  * def productSchema = read('classpath:schemas/product-schema.json')

Scenario: Validate product list schema
  Given path '/products'
  When method GET
  Then status 200

  # Validate entire response schema
  And match each response == productSchema

Scenario: Detect breaking changes (strict contract)
  Given path '/products'
  When method GET
  Then status 200

  # Required fields must exist
  And match response[0].id != null
  And match response[0].name != null
  And match response[0].price != null

Scenario: Validate data types (contract enforcement)
  Given path '/products'
  When method GET
  Then status 200

  And match response[0].id == '#number'
  And match response[0].name == '#string'
  And match response[0].price == '#number'