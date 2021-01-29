package com.example.demo;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "news")
public class NewsDto {

    @Id @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "news_id_seq")
    @SequenceGenerator(name = "news_id_seq", sequenceName = "news_id_seq", allocationSize = 1)
    private Long id;

    @Column(length = 512)
    private String title;

    @Column(length = 65536)
    private String content;
    private String category;
}
