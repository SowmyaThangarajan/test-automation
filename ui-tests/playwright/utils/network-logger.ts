import { Page } from '@playwright/test';

export class NetworkLogger {
  static observeMicroservices(page: Page) {
    page.on('requestfailed', request => {
      console.log(`❌ Service Call Failed: ${request.url()} | Error: ${request.failure()?.errorText}`);
    });

    page.on('response', async response => {
      if (response.url().includes('/api/v1/') && response.status() >= 400) {
        const body = await response.text();
        console.error(`⚠️ Microservice Error [${response.status()}] at ${response.url()}: ${body}`);
      }
    });
  }
}
