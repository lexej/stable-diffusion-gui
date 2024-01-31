const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy:{
      "/api": {
        target: "http://backend-service:5000",
        changeOrigin: true,
        secure: false,
      }
    }
  } //  IMPORTANT: Listen on 0.0.0.0:8080 (-> available from other IPs)
})
