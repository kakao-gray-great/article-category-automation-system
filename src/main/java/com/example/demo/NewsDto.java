package com.example.demo;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "news")
public class NewsDto {

    @Id @GeneratedValue
    @SequenceGenerator(name = "news_id_seq", sequenceName = "news_id_seq",  allocationSize = 1)
    private Long id;
    private String title;
    private String content;
    private String category;
}
