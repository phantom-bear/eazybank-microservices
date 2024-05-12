package com.eazybytes.accounts.service;

import com.eazybytes.accounts.dto.CustomerDetailsDto;

public interface ICustomerService {
    /**
     * 
     * TODO
     * @author ZhangDianxiong
     * @date 2024-05-03 19:09:34
     * @param: mobileNumber
     * @return 
     **/

    CustomerDetailsDto fetchCustomerDetails(String mobileNumber, String correlationId);
}
