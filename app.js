const request = require('request');
const cheerio = require('cheerio');

const crawlingByBreakingnews = () => {
    const category = 'society';
    // const category = 'politics';
    let count = 0;
    for(let day = 1; day <= 20; day++) {
        for(let page = 1; page <= 5; page++) {
            // console.log(`https://news.daum.net/breakingnews/${category}?page=${page}&regDate=202006${pad(day, 2)}`);
            request(`https://news.daum.net/breakingnews/${category}?page=${page}&regDate=202006${pad(day, 2)}`, (error, response, body) => {
                
                if(body) {
                    const $ = cheerio.load(body);

                    let aArr;
                    aArr = $('a');
                
                    let newsArr = [];

                    for(let i = 0; i < aArr.length; i++) {
                        if(aArr[i].attribs.href.includes("v.daum.net/v/202006") )
                            newsArr.push(aArr[i].attribs.href);
                    }

                    newsArr = Array.from(new Set(newsArr));

                    
                    for(let i = 0; i < newsArr.length; i++) {
                        console.log(count++, newsArr[i]);
                        crawlingByNewsByUrl(newsArr[i]);
                    }

                } else {
                    return;
                }       
            });
        }
    }
}

const crawlingByNewsByUrl = (url) => {
    // console.log(url);
    request(url, (error, response, body) => {
        if(body) {
            const $ = cheerio.load(body);

            let title = $('.tit_view')[0].children[0].data;
            let contentArr = $('#harmonyContainer p');
            let content = "";
            for(let i = 0; i < contentArr.length; i++) {
                if(contentArr[i].children[0] === undefined || contentArr[i].children[0].data === undefined) {
                    console.log(`[CONTINUE] contentArr[${i}].children[0].data === undefined`);
                    continue;
                }
                content += contentArr[i].children[0].data + " ";
            }

            let category = $('.gnb_comm')[0].attribs['data-category'];

            let newsObject = {
                title, 
                content,
                category
            }
            console.log(newsObject);
            globalChannel.sendToQueue(queueName, Buffer.from(JSON.stringify(newsObject)));

        } else {
            return;
        }
        
    });
}

let globalChannel;

const amqp = require('amqplib/callback_api');
const queueName = 'PRE_NEWS';
amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        channel.assertQueue(queueName, {
            durable: true
        });
        globalChannel = channel;

        crawlingByBreakingnews();
    });
});

const pad = (n, width, z) => {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}
