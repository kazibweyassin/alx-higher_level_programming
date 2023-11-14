#!/usr/bin/node

class Rectangle {
	  constructor (width, height) {
		      if (width > 0 && height > 0) {
			            this.width = width;
			            this.height = height;
			          }
		    }

	  print () {
		      const x = this.width;
		      let y = this.height;
		      while (y > 0) {
			            console.log('X'.repeat(x));
			            y = y - 1;
			          }
		    }
		rotate () {
					this.height = this.width ^ this.height;
					this.width = this.height ^ this.width;
					this.height = this.width ^ this.height;
				}
		double () {
					this.height = this.height * 2;
					this.width = this.width * 2;
				}
}
module.exports = Rectangle;
