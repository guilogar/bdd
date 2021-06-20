'use strict';

const { NegativeRadius } = require('./exceptions/negative-radius');

const radiusArea = (radius = 0.1) =>  {
  if (radius <= 0) {
    throw new NegativeRadius('Negative Radius');
  } else {
    return (radius * radius * Math.PI);
  }
};

module.exports = {
  radiusArea
};