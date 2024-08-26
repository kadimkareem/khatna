/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { CarType } from './CarType';

export type CreateCar = {
    license_plate: (string | null);
    model: (string | null);
    year: (number | null);
    color: (string | null);
    photo: (string | null);
    capacity: number;
    type: CarType;
};

