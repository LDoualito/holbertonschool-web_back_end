const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('checks output with positive numbers', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(1, 2), 3);
    assert.strictEqual(calculateNumber(3, 5), 8);
    assert.strictEqual(calculateNumber(4, 7), 11);
    assert.strictEqual(calculateNumber(0, 1.6), 2);
    assert.strictEqual(calculateNumber(0.4, 8), 8);
    assert.strictEqual(calculateNumber(10, 2.7), 13);
    assert.strictEqual(calculateNumber(9.1, 9.9), 19);
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
  });
  it('checks output with negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, -2), -3);
    assert.strictEqual(calculateNumber(-6, -3), -9);
    assert.strictEqual(calculateNumber(-1.1, -2.3), -3);
    assert.strictEqual(calculateNumber(-5.8, -2), -8);
    assert.strictEqual(calculateNumber(-1, -8.4), -9);
    assert.strictEqual(calculateNumber(-1, 2.6), 2);
  });
  it('checks output with wrong argument', () => {
    assert.strictEqual(calculateNumber(NaN, 3.6), NaN);
    assert.strictEqual(calculateNumber(3.6, NaN), NaN);
    assert.strictEqual(calculateNumber(NaN, NaN), NaN);
  });
});
