import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { ProductPage } from '../pages/ProductPage';
import { PaymentPage } from '../pages/PaymentPage';

// Declare the types of your fixtures
type MyFixtures = {
  loginPage: LoginPage;
  productPage: ProductPage;
  paymentPage: PaymentPage;
};

// Extend the base test to include our POMs
export const test = base.extend<MyFixtures>({
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },
  productPage: async ({ page }, use) => {
    await use(new ProductPage(page));
  },
  paymentPage: async ({ page }, use) => {
    await use(new PaymentPage(page));
  },
});

export { expect } from '@playwright/test';