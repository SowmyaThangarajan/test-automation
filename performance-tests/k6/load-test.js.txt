import http from 'k6/http';
import { check, sleep } from 'k6';

// Configuration
export const options = {
  stages: [
    { duration: '1m', target: 200 },   // ramp-up
    { duration: '2m', target: 1000 },  // peak load (1000 users)
    { duration: '1m', target: 0 },     // ramp-down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // P95 latency < 500ms
    http_req_failed: ['rate<0.01'],    // error rate < 1%
  },
};

// Base URL
const BASE_URL = 'https://api.demo.com';

// Simulated user journey
export default function () {

  // 🔐 Login
  let loginRes = http.post(`${BASE_URL}/login`, JSON.stringify({
    username: 'test',
    password: 'test'
  }), {
    headers: { 'Content-Type': 'application/json' },
  });

  check(loginRes, {
    'login successful': (r) => r.status === 200,
  });

  let token = loginRes.json('token');

  // 🔍 Search product
  let searchRes = http.get(`${BASE_URL}/products?query=phone`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  check(searchRes, {
    'search success': (r) => r.status === 200,
  });

  // 🛒 Checkout
  let checkoutRes = http.post(`${BASE_URL}/checkout`, JSON.stringify({
    productId: 1,
    quantity: 1
  }), {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });

  check(checkoutRes, {
    'checkout success': (r) => r.status === 200,
  });

  // 💳 Payment
  let paymentRes = http.post(`${BASE_URL}/payment`, JSON.stringify({
    amount: 100
  }), {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  });

  check(paymentRes, {
    'payment success': (r) => r.status === 200,
  });

  sleep(1);
}