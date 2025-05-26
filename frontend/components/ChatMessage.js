export default {
    props: ['message'],
    template: `
        <div class="message">
            <span :class="message.role">{{ message.role }}:</span>
            <span v-if="message.isHtml" v-html="message.content"></span>
            <span v-else>{{ message.content }}</span>
        </div>
    `
};
