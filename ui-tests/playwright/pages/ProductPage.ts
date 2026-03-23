import { Page, Locator } from '@playwright/test';

export class ProductPage {
  readonly page: Page;
  readonly searchInput: Locator;
  readonly searchBtn: Locator;
  readonly addToCartBtn: Locator;

  constructor(page: Page) {
    this.page = page;
    this.searchInput = page.locator('#search');
    this.searchBtn = page.locator('#searchBtn');
    this.addToCartBtn = page.locator('#addToCart');
  }

  async searchProduct(name: string) {
    await this.searchInput.fill(name);
    await this.searchBtn.click();
    // Dynamic: Click the first product visible in the results
    await this.page.locator('.product').first().click();
  }

  async addToCart() {
    await this.addToCartBtn.click();
    await this.page.locator('#checkout').click();
  }
}