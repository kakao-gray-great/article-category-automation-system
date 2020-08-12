package com.example.demo;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RabbitConsumer {

    @Autowired
    NewsDtoRepository newsDtoRepository;

    @RabbitListener(queues = "PRE_NEWS")
    public void receiveMessage(final String message) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        NewsDto newsDto = objectMapper.readValue(message, NewsDto.class);
        newsDtoRepository.save(newsDto);
        System.out.println("newsDto = " + newsDto);
    }
}

