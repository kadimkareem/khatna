/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { PassengerType } from './PassengerType';

export type CreatePassenger = {
    type: PassengerType;
    location: string;
    distination: string;
    payment_method: string;
    pickup_date: string;
    pickup_time: string;
    pickup_location: string;
    return_date: string;
    return_time: string;
    service_hours: number;
};

