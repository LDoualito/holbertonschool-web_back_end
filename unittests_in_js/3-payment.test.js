const { expect } = require('chai');
const sinon = require('sinon');
const utils = require('./utils');

const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('Result of payment is the same as the function', () => {
    const functionSpy = sinon.spy(utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');
    
    const apiResult = sendPaymentRequestToApi(100, 20);
    
    expect(functionSpy.calledOnceWith('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.equal(true);
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(apiResult);
    
    functionSpy.restore();
    consoleSpy.restore();
  });
});
