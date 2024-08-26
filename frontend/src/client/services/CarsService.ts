/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CarOut } from '../models/CarOut';
import type { CarsOut } from '../models/CarsOut';
import type { CreateCar } from '../models/CreateCar';
import type { Message } from '../models/Message';
import type { UpdateCar } from '../models/UpdateCar';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class CarsService {

    /**
     * Read Cars
     * Retrieve cars.
     * @returns CarsOut Successful Response
     * @throws ApiError
     */
    public static carsReadCars({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<CarsOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/cars/',
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
     * Create Car
     * Create new car.
     * @returns CreateCar Successful Response
     * @throws ApiError
     */
    public static carsCreateCar({
        requestBody,
    }: {
        requestBody: CreateCar,
    }): CancelablePromise<CreateCar> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/cars/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Car
     * Get car by ID.
     * @returns CarOut Successful Response
     * @throws ApiError
     */
    public static carsReadCar({
        id,
    }: {
        id: number,
    }): CancelablePromise<CarOut> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/cars/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Car
     * Update an car.
     * @returns UpdateCar Successful Response
     * @throws ApiError
     */
    public static carsUpdateCar({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: UpdateCar,
    }): CancelablePromise<UpdateCar> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/cars/{id}',
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
     * Delete Car
     * Delete an car.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static carsDeleteCar({
        id,
    }: {
        id: number,
    }): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/cars/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
