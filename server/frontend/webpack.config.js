const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx"], // Add the .ts and .tsx extensions
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/, // Update the test to include .ts and .tsx files
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
        
      },
      {
        test: /\.css$/, // Add a rule to handle CSS files
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("development"),
    }),
  ],
  watch: true
};
