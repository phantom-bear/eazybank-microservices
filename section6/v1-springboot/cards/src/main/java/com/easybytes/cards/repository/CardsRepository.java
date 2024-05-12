package com.easybytes.cards.repository;

import com.easybytes.cards.entity.Cards;
import org.springframework.data.repository.CrudRepository;

import java.util.Optional;


public interface CardsRepository extends CrudRepository<Cards, Long> {

    Optional<Cards> findByMobileNumber(String mobileNumber);

    Optional<Cards> findByCardNumber(String cardNumber);
}
