Feature: Product API Contract Validation

Background:
  * url baseUrl
  * def productSchema = read('classpath:schemas/product-schema.json')

Scenario: Validate product list schema (strict)
  Given path '/products'
  When method GET
  Then status 200

  # Validate entire response schema
  And match each response contains only productSchema

Scenario: Detect breaking changes (strict contract)
  Given path '/products'
  When method GET
  Then status 200

  And match each response ==
  """
  {
    id: '#number',
    name: '#string',
    price: '#number',
    description: '##string'   # optional
  }
  """

Scenario: Validate data types (contract enforcement)
  Given path '/products'
  When method GET
  Then status 200

  And match response[0].id == '#number'
  And match response[0].name == '#string'
  And match response[0].price == '#number'