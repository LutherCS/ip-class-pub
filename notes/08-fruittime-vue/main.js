const { createApp, ref, reactive } = Vue

createApp({
    setup() {
        const appName = ref('fruiTime!')
        return {
            appName
        }
    }
}).mount('#titleCard')

const app = createApp({
    setup() {
        const basket = reactive([
            { name: "Apple", rating: 3 },
            { name: "Banana", rating: 3 },
            { name: "Cherry", rating: 3 },
            { name: "Durian", rating: 3 },
        ]);

        return { basket }
    }
})
app.mount("#app");