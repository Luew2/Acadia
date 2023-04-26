module.exports = {
  async rewrites() {
    return [
      {
        source: '/generate-sticker',
        destination: 'http://localhost:5000/generate-sticker',
      },
      {
        source: '/Sticker_Generator/data/:path*',
        destination: 'http://localhost:5000/Sticker_Generator/data/:path*',
      },
    ];
  },
};
