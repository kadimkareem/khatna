/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreatePassenger } from '../models/CreatePassenger';
import type { Message } from '../models/Message';
import type { Passenger } from '../models/Passenger';
import type { PassengerList } from '../models/PassengerList';
import type { UpdatePassenger } from '../models/UpdatePassenger';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class PassengersService {

    /**
     * Read Passengers
     * Retrieve passengers. only super user can fetch all
     * @returns PassengerList Successful Response
     * @throws ApiError
     */
    public static readPassengers({
        skip,
        limit = 100,
    }: {
        skip?: number,
        limit?: number,
    }): CancelablePromise<PassengerList> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/passengers/',
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
     * Create Passenger
     * Create new passenger.
     * @returns CreatePassenger Successful Response
     * @throws ApiError
     */
    public static createPassenger({
        requestBody,
    }: {
        requestBody: CreatePassenger,
    }): CancelablePromise<CreatePassenger> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/passengers/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Read Passenger
     * Get passenger by ID.
     * @returns Passenger Successful Response
     * @throws ApiError
     */
    public static readPassenger({
        id,
    }: {
        id: number,
    }): CancelablePromise<Passenger> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/passengers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Update Passenger
     * Update an passenger.
     * @returns UpdatePassenger Successful Response
     * @throws ApiError
     */
    public static updatePassenger({
        id,
        requestBody,
    }: {
        id: number,
        requestBody: UpdatePassenger,
    }): CancelablePromise<UpdatePassenger> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/api/v1/passengers/{id}',
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
     * Delete Passenger
     * Delete an passenger.
     * @returns Message Successful Response
     * @throws ApiError
     */
    public static deletePassenger({
        id,
    }: {
        id: number,
    }): CancelablePromise<Message> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/api/v1/passengers/{id}',
            path: {
                'id': id,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
