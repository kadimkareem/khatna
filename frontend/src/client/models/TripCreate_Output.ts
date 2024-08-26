/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Passenger } from './Passenger';
import type { TripStatus } from './TripStatus';
import type { TripType } from './TripType';

export type TripCreate_Output = {
    route_id: number;
    car_id: number;
    estimation: string;
    cost: number;
    tripStatus: TripStatus;
    type: TripType;
    passengers_count?: (number | null);
    passengers?: (Array<Passenger> | null);
};

