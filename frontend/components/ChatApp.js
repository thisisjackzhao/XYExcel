import ChatMessage from './ChatMessage.js';

export default {
    components: { ChatMessage },
    data() {
        return {
            ws: null,
            input: '',
            messages: [],
            file: null
        };
    },
    mounted() {
        this.connect();
    },
    methods: {
        connect() {
            this.ws = new WebSocket('ws://localhost:8000/ws');
            this.ws.onmessage = (e) => {
                const msg = JSON.parse(e.data);
                if (msg.type === 'image') {
                    this.messages.push({ role: 'bot', content: `<img src="${msg.data}" />`, isHtml: true });
                } else {
                    this.messages.push({ role: 'bot', content: msg.data });
                }
            };
        },
        async sendMessage() {
            const text = this.input.trim();
            if (!text || !this.ws) return;
            this.messages.push({ role: 'user', content: text });
            this.ws.send(text);
            this.input = '';
        },
        uploadFile(event) {
            this.file = event.target.files[0];
        },
        async sendFile() {
            if (!this.file) return;
            const form = new FormData();
            form.append('file', this.file);
            await fetch('/upload', { method: 'POST', body: form });
            this.messages.push({ role: 'bot', content: 'File uploaded.' });
        }
    },
    template: `
        <div>
            <h2>XYExcel Chat</h2>
            <input type="file" @change="uploadFile" />
            <button @click="sendFile">Upload</button>
            <div class="messages">
                <ChatMessage v-for="(m, i) in messages" :key="i" :message="m" />
            </div>
            <form @submit.prevent="sendMessage">
                <input type="text" v-model="input" placeholder="Type your message" required>
                <button type="submit">Send</button>
            </form>
        </div>
    `
};
