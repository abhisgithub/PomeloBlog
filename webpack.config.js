const Dotenv = require('dotenv-webpack');

module.exports = {
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader"
				}
			}
		]
	},

	node: {
		fs: "empty"
	  },

	plugins: [
	new Dotenv()
	]
}