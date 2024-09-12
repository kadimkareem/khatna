/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Driver } from '../models/Driver';
import type { DriverCreate } from '../models/DriverCreate';
import type { DriverList } from '../models/DriverList';
import type { DriverUpdate } from '../models/DriverUpdate';
import type { Message } from '../models/Message';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DriversService {

    /**
     * Read Drivers
     * Retrieve drivers.
     * @returns DriverList Successful Response
     * @throws ApiError
     */
    public static readDrivers({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<DriverList> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/drivers/',
            query: {
                'skip': skip,
                'limit': limit,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Create Driver
     * Create new driver.
     * @returns DriverCreate Successful Response
     * @throws ApiError
     */
    public static createDriver({
        requestBody,
    }: {
        requestBody: DriverCreate,
    }): CancelablePromise<DriverCreate> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/drivers/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Driver
     * Get driver by ID.
     * @returns Driver Successful Response
     * @throws ApiError
     */
    public static readDriver({
        id,
    }: {
        id: number,
    }): CancelablePromise<Driver> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/drivers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Driver
     * Update an driver.
     * @returns DriverUpdate Successful Response
     * @throws ApiError
     */
    public static updateDriver({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: DriverUpdate,
    }): CancelablePromise<DriverUpdate> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/drivers/{id}',
            path: {
                'id': id,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Delete Driver
     * Delete an driver.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deleteDriver({
        id,
    }: {
        id: number,
    }): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/drivers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Driver Rating
     * Update an driver rating. only passengers can update rating
     * @returns any Successful Response
     * @throws ApiError
     */
    public static updateDriverRating({
        id,
        rating,
    }: {
        id: number,
        rating: number,
    }): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/drivers/rating/{id}',
            path: {
                'id': id,
            },
            query: {
                'rating': rating,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
