import { defineConfig, devices } from '@playwright/test';
// import dotenv from 'dotenv';
import path from 'path';

/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// dotenv.config({ path: path.resolve(__dirname, '.env') });

export default defineConfig({
  testDir: './tests',
  
  /* 1. Parallel Execution Pipeline */
  // Run tests in files in parallel
  fullyParallel: true,
  // Fail the build on CI if you accidentally left test.only in the source code.
  forbidOnly: !!process.env.CI,
  // Maximize workers based on CI or local CPU cores
  workers: process.env.CI ? 4 : undefined,

  /* 2. Retry Logic for Flaky Tests */
  // Retry on CI to account for microservice/network hiccups
  retries: process.env.CI ? 2 : 1,

  /* 3. Reporting & Artifacts */
  reporter: [
    ['html'],
    ['list'],
    ['junit', { outputFile: 'results/results.xml' }],
    ['allure-playwright']
  ],

  /* 4. Shared Settings for all projects */
  use: {
    /* Base URL for the API Gateway / Frontend */
    baseURL: process.env.BASE_URL || 'https://www.saucedemo.com/',

    /* 5. Screenshot & Video Capture for Failures */
    trace: 'retain-on-failure',      // Records DOM, Network, and Console
    screenshot: 'only-on-failure',   // Snapshots of the crash
    video: 'on-first-retry',         // Video of the failed interaction
    
    /* Global timeout for each action (click, fill, etc) */
    actionTimeout: 10000,
    navigationTimeout: 15000,
  },

  /* 6. Multi-Browser / Multi-Device Testing */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },
    // {
    //   name: 'webkit',
    //   use: { ...devices['Desktop Safari'] },
    // },

    // /* Test against mobile viewports (important for E-commerce) */
    // {
    //   name: 'Mobile Chrome',
    //   use: { ...devices['Pixel 5'] },
    // },
  ],

  /* 7. Local Dev Server (Optional) */
  // Run your local frontend before tests start
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://127.0.0.1:3000',
  //   reuseExistingServer: !process.env.CI,
  // },
});
