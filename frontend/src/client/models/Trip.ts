/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { TripStatus } from './TripStatus';
import type { TripType } from './TripType';

export type Trip = {
    estimation?: (string | null);
    cost?: (number | null);
    trip_status?: (TripStatus | null);
    type?: (TripType | null);
    passengers_count?: (number | null);
    id?: (number | null);
    driver_id?: (number | null);
    passenger_id?: (number | null);
    route_id?: (number | null);
    car_id?: (number | null);
    created_at?: (string | null);
    updated_at?: (string | null);
};

