const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('when type is SUM', () => {
    it('it round the first argument', () => {
        expect(calculateNumber('SUM', 1.0, 0)).to.equal(1);
        expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
        expect(calculateNumber('SUM', 1.7, 0)).to.equal(2);
    });
    
    it('it round the second argument', () => {
        expect(calculateNumber('SUM', 0, 1.0)).to.equal(1);
        expect(calculateNumber('SUM', 0, 1.3)).to.equal(1);
        expect(calculateNumber('SUM', 0, 1.7)).to.equal(2);
    });
    
    it('it should return the right number', () => {
        expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
        expect(calculateNumber('SUM', 0, 1.2)).to.equal(1);
        expect(calculateNumber('SUM', 1.3, 1.3)).to.equal(2);
        expect(calculateNumber('SUM', 1.7, 1.2)).to.equal(3);
        expect(calculateNumber('SUM', 1.3, 1.8)).to.equal(3);
        expect(calculateNumber('SUM', 1.6, 1.8)).to.equal(4);
    });
  });

  describe('when type is SUBTRACT', () => {
    it('it round the first argument', () => {
        expect(calculateNumber('SUBTRACT', 1.0, 0)).to.equal(1);
        expect(calculateNumber('SUBTRACT', 1.3, 0)).to.equal(1);
        expect(calculateNumber('SUBTRACT', 1.7, 0)).to.equal(2);
    });
    
    it('it round the second argument', () => {
        expect(calculateNumber('SUBTRACT', 0, 1.0)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 0, 1.3)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 0, 1.7)).to.equal(-2);
    });
    
    it('it should return the right number', () => {
        expect(calculateNumber('SUBTRACT', 1.3, 0)).to.equal(1);
        expect(calculateNumber('SUBTRACT', 0, 1.2)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 1.3, 1.3)).to.equal(0);
        expect(calculateNumber('SUBTRACT', 1.7, 1.2)).to.equal(1);
        expect(calculateNumber('SUBTRACT', 1.3, 1.8)).to.equal(-1);
        expect(calculateNumber('SUBTRACT', 1.6, 1.8)).to.equal(0);
    });
  });

  describe('when type is DIVIDE', () => {
    it('it round the first argument', () => {
        expect(calculateNumber('DIVIDE', 10.0, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.3, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.7, 2)).to.equal(5.5);
    });
    
    it('it round the second argument', () => {
        expect(calculateNumber('DIVIDE', 10, 1.0)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10, 1.3)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10, 1.7)).to.equal(5);
    });
    
    it('it should return the right number', () => {
        expect(calculateNumber('DIVIDE', 10.3, 2)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10, 1.2)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10.3, 1.3)).to.equal(10);
        expect(calculateNumber('DIVIDE', 10.7, 1.2)).to.equal(11);
        expect(calculateNumber('DIVIDE', 10.3, 1.8)).to.equal(5);
        expect(calculateNumber('DIVIDE', 10.6, 1.8)).to.equal(5.5);
    });

    it('it should return Erro).to.equal(expect to 0', () => {
        expect(calculateNumber('DIVIDE', 10.3, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 10.7, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 10.3, 0.3)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 10.7, 0.2)).to.equal('Error');
    });
  });
});
