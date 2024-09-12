import React from 'react'
import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from '@chakra-ui/react'
import { SubmitHandler, useForm } from 'react-hook-form'

import { useMutation, useQueryClient } from 'react-query'
import { ApiError, CarOut, UpdateCar, CarsService } from '../../client'
import useCustomToast from '../../hooks/useCustomToast'

interface EditCarProps {
  car: CarOut
  isOpen: boolean
  onClose: () => void
}

const EditCar: React.FC<EditCarProps> = ({ car, isOpen, onClose }) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors, isDirty },
  } = useForm<UpdateCar>({
    mode: 'onBlur',
    criteriaMode: 'all',
    defaultValues: car,
  })

  const updateCar = async (data: UpdateCar) => {
    await CarsService.updateCar({ id: car.id, requestBody: data })
  }

  const mutation = useMutation(updateCar, {
    onSuccess: () => {
      showToast('Success!', 'Car updated successfully.', 'success')
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = err.body.detail
      showToast('Something went wrong.', `${errDetail}`, 'error')
    },
    onSettled: () => {
      queryClient.invalidateQueries('cars')
    },
  })

  const onSubmit: SubmitHandler<UpdateCar> = async (data) => {
    mutation.mutate(data)
  }

  const onCancel = () => {
    reset()
    onClose()
  }

  return (
    <>
      <Modal
        isOpen={isOpen}
        onClose={onClose}
        size={{ base: 'sm', md: 'md' }}
        isCentered
      >
        <ModalOverlay />
        <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>Edit Car</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isInvalid={!!errors.capacity}>
              <FormLabel htmlFor="title">Capacity</FormLabel>
              <Input
                id="capacity"
                {...register('capacity', {
                  required: 'capacity is required',
                })}
                type="text"
              />
              {errors.capacity && (
                <FormErrorMessage>{errors.capacity.message}</FormErrorMessage>
              )}
            </FormControl>
            {/* <FormControl mt={4}>
              <FormLabel htmlFor="description">Description</FormLabel>
              <Input
                id="description"
                {...register('description')}
                placeholder="Description"
                type="text"
              />
            </FormControl> */}
          </ModalBody>
          <ModalFooter gap={3}>
            <Button
              variant="primary"
              type="submit"
              isLoading={isSubmitting}
              isDisabled={!isDirty}
            >
              Save
            </Button>
            <Button onClick={onCancel}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default EditCar
