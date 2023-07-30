const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('Result of payment is the same as the function', () => {
    const functionStub = sinon.stub(Utils, 'calculateNumber');
    functionStub.returns(10);
    const consoleSpy = sinon.spy(console, 'log');
    
    const apiResult = sendPaymentRequestToApi(100, 20);
    
    expect(functionStub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.equal(true);
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(apiResult);
    
    functionStub.restore();
    consoleSpy.restore();
  });
});
