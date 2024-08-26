/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Passenger } from './Passenger';
import type { TripStatus } from './TripStatus';
import type { TripType } from './TripType';

export type TripUpdate_Output = {
    route_id?: (number | null);
    car_id?: (number | null);
    estimation?: (string | null);
    cost?: (number | null);
    tripStatus?: (TripStatus | null);
    type?: (TripType | null);
    passengers?: (Array<Passenger> | null);
    passengers_count?: (number | null);
};

