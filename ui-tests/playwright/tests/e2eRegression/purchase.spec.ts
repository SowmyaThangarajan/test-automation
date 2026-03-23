import { test, expect } from '../../fixtures/baseFixture';
import { TEST_DATA } from '../../test-data/testData';

test.describe('E-Commerce Core Flows', () => {

  test('User can complete E2E Purchase Flow with static account', async ({ 
    page, 
    loginPage, 
    productPage, 
    paymentPage 
  }) => {
    
    // 1. Auth Service Flow
    await page.goto('/');
    await page.click('#login');
    await loginPage.login(TEST_DATA.user.username, TEST_DATA.user.password);

    // 2. Product Service Flow
    await productPage.searchProduct(TEST_DATA.inventory.searchQuery);
    await productPage.addToCart();

    // 3. Payment Service Flow
    const response = await paymentPage.executePayment(TEST_DATA.payment.cardNumber);
    
    // Validate the microservice response directly
    expect(response.status()).toBe(200);

    // 4. Order Confirmation Assertion
    const confirmation = page.locator(TEST_DATA.selectors.confirmationId);
    await expect(confirmation).toBeVisible({ timeout: 10000 });
    await expect(confirmation).toContainText(TEST_DATA.selectors.successMessage);
  });

});