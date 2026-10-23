import test from 'node:test';
import assert from 'node:assert/strict';
import { app } from './server.js';

// Route integration can be exercised with a live server; this test verifies module export.
test('express application is exported', () => {
  assert.equal(typeof app, 'function');
});
