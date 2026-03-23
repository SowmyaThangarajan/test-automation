export const TEST_DATA = {
    // Credentials for Auth Service
    user: {
      username: 'testuser',
      password: 'Password123',
    },
    // Search terms for Product Service
    inventory: {
      searchQuery: 'Laptop',
      expectedProduct: 'Gaming Laptop Pro',
    },
    // Payment Details for Payment Service
    payment: {
      cardNumber: '4111111111111111',
      expiry: '12/28',
      cvv: '123'
    },
    // UI Assertions
    selectors: {
      confirmationId: '#orderConfirmation',
      successMessage: 'Success',
    }
  };
  