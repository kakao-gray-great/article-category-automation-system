const amqp = require('amqplib/callback_api');

let exportsChannel;

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var queue = 'PRE_NEWS';

        channel.assertQueue(queue, {
            durable: false
        });
        // channel.sendToQueue(queue, Buffer.from(msg));

        exportsChannel = channel;

    });
});

module.exports = {
    channel : exportsChannel
}