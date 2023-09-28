"use strict";

const { createApp, ref, reactive } = Vue

const app = createApp({
    setup() {
        const message = ref('Hello CS330!');
        const title = ref(`This page has been loaded on ${new Date().toLocaleString()}`);
        return {
            message, title
        }
    }
});

app.mount('#app');

createApp({
    setup() {
        const collection = reactive([
            { type: "Limestone", weight: 10, quantity: 20 },
            { type: "Marble", weight: 100, quantity: 2 }
        ])

        return {
            collection
        }
    }
}).mount("#inventory")