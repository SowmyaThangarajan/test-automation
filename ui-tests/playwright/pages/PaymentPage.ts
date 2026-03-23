import { Page, Locator } from '@playwright/test';

export class PaymentPage {
  readonly page: Page;
  readonly cardNumberInput: Locator;
  readonly payButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.cardNumberInput = page.locator('#cardNumber');
    this.payButton = page.locator('#pay');
  }

  async executePayment(card: string) {
    await this.cardNumberInput.fill(card);
    
    // Capturing the network call to the Payment Service for debugging
    const [response] = await Promise.all([
      this.page.waitForResponse(res => res.url().includes('/api/pay') && res.status() === 200),
      this.payButton.click(),
    ]);
    
    return response;
  }
}