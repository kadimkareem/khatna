/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { PassengerType } from './PassengerType';

export type UpdatePassenger = {
    type?: (PassengerType | null);
    location?: (string | null);
    distination?: (string | null);
    payment_method?: (string | null);
    pickup_date?: (string | null);
    pickup_time?: (string | null);
    pickup_location?: (string | null);
    return_date?: (string | null);
    return_time?: (string | null);
    service_hours?: (number | null);
};

